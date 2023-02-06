package reboot;

import javax.net.ssl.*;
import java.io.*;
import java.net.InetAddress;
import java.net.URL;
import java.net.URLConnection;
import java.net.UnknownHostException;
import java.security.cert.X509Certificate;
import java.time.ZonedDateTime;
import java.util.LinkedHashMap;
import java.util.Map;
import java.util.Objects;

import static java.lang.Math.max;

public class RebootUtil {

    public static final String SRC_MAIN_REBOOT_AT_TXT = "src/main/rebootAt.txt";


    public static class HostName {
        public final String value;

        public HostName(String value) {
            this.value = value.split("\\.")[0].toLowerCase();
        }

        public static HostName localHostName() {
            try {
                return new HostName(InetAddress.getLocalHost().getHostName());
            } catch (UnknownHostException e) {
                throw new RuntimeException("Unable to resolve local host name", e);
            }
        }

        @Override
        public String toString() {
            return value;
        }

        @Override
        public boolean equals(Object o) {
            if (this == o) return true;
            if (o == null || getClass() != o.getClass()) return false;
            HostName hostName = (HostName) o;
            return Objects.equals(value, hostName.value);
        }

        @Override
        public int hashCode() {
            return Objects.hash(value);
        }
    }

    public static void useSystemProxies() {
        System.setProperty("java.net.useSystemProxies", "true");
    }

    public static void addGenericSSLCertificate() {
        try {
            // Create a trust manager that does not validate certificate chains
            TrustManager[] trustAllCerts = new TrustManager[] {new X509TrustManager() {
                public java.security.cert.X509Certificate[] getAcceptedIssuers() {
                    return null;
                }
                public void checkClientTrusted(X509Certificate[] certs, String authType) {
                }
                public void checkServerTrusted(X509Certificate[] certs, String authType) {
                }
            }
            };

            // Install the all-trusting trust manager
            SSLContext sc = SSLContext.getInstance("SSL");
            sc.init(null, trustAllCerts, new java.security.SecureRandom());
            HttpsURLConnection.setDefaultSSLSocketFactory(sc.getSocketFactory());

            // Create all-trusting host name verifier
            HostnameVerifier allHostsValid = new HostnameVerifier() {
                public boolean verify(String hostname, SSLSession session) {
                    return true;
                }
            };

            // Install the all-trusting host verifier
            HttpsURLConnection.setDefaultHostnameVerifier(allHostsValid);

        } catch (Exception e) {
            throw new RuntimeException(e);
        }
    }

    public static Map<HostName, ZonedDateTime> readRebootTimes(URL fileURL) {
        Map<HostName, ZonedDateTime> rebootTimes = new LinkedHashMap<>();

        try (InputStream inputStream = fileURL.openStream()) {
            String content = new String(inputStream.readAllBytes());
            for (String line : content.split("\n")) {
                if (!line.contains("|")) {
                    continue;
                }

                String[] parts = line.split("\\|");
                HostName hostname = new HostName(parts[0]);
                ZonedDateTime rebootTime = ZonedDateTime.parse(parts[1]);

                rebootTimes.merge(hostname, rebootTime, (oldTime, newTime) -> {
                    ZonedDateTime now = ZonedDateTime.now();
                    if (oldTime.isAfter(now)) {
                        if (newTime.isAfter(oldTime) || newTime.isBefore(now)) {
                            return oldTime;
                        } else {
                            return newTime;
                        }
                    } else if (newTime.isAfter(oldTime)) {
                        return newTime;
                    } else {
                        return oldTime;
                    }
                });
            }
        } catch (Exception e) {
            throw new RuntimeException("Failed to read reboot timings", e);
        }

        return rebootTimes;
    }

    public static Map<HostName, ZonedDateTime> readRebootTimes() {
        URL timingsUrl;
        try {
            timingsUrl = new URL("https://raw.githubusercontent.com/MatejTymes/Playground/master/" + SRC_MAIN_REBOOT_AT_TXT);
        } catch (Exception e) {
            throw new RuntimeException("Failed to parse timings URL", e);
        }
        return readRebootTimes(timingsUrl);
    }

    public static void writeRebootTimes(Map<HostName, ZonedDateTime> rebootTimes) throws IOException {
        File file = new File(SRC_MAIN_REBOOT_AT_TXT);

        try (BufferedWriter writer = new BufferedWriter(new FileWriter(file))) {
            for (Map.Entry<HostName, ZonedDateTime> entry : rebootTimes.entrySet()) {
                HostName hostName = entry.getKey();
                ZonedDateTime rebootTime = entry.getValue();

                writer.write(hostName.value + "|" + rebootTime + "\n");
            }
            writer.flush();
        }
    }

    public static void triggerRebootAt(ZonedDateTime rebootAt) {
        ZonedDateTime now = ZonedDateTime.now();

        long rebootInSeconds = max(
                0L,
                (rebootAt.toInstant().toEpochMilli() - now.toInstant().toEpochMilli()) / 1_000
        );

        try {
            Runtime.getRuntime().exec("shutdown -r -t " + rebootInSeconds);
        } catch (Exception e) {
            throw new RuntimeException("Failed to execute shutdown", e);
        }
    }
}
