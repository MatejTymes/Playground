package reboot;

import java.io.InputStream;
import java.net.URL;
import java.time.ZonedDateTime;
import java.util.Map;
import java.util.TreeMap;

import static java.lang.Math.max;

public class RebootUtil {


    public static Map<String, ZonedDateTime> readRebootTimes(URL fileURL) {
        Map<String, ZonedDateTime> rebootTimes = new TreeMap<>();

        try (InputStream inputStream = fileURL.openStream()) {
            String content = new String(inputStream.readAllBytes());
            for (String line : content.split("\n")) {
                if (!line.contains("|")) {
                    continue;
                }

                String[] parts = line.split("\\|");
                String hostname = parts[0].toLowerCase();
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

    public static Map<String, ZonedDateTime> readRebootTimes() {
        URL timingsUrl;
        try {
            timingsUrl = new URL("https://raw.githubusercontent.com/MatejTymes/Playground/master/src/main/rebootAt.txt");
        } catch (Exception e) {
            throw new RuntimeException("Failed to parse timings URL", e);
        }
        return readRebootTimes(timingsUrl);
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
