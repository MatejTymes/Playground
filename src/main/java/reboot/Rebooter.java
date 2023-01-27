package reboot;

import reboot.RebootUtil.HostName;

import java.time.ZonedDateTime;
import java.util.Map;
import java.util.concurrent.ScheduledExecutorService;
import java.util.concurrent.TimeUnit;

import static java.util.concurrent.Executors.newScheduledThreadPool;
import static reboot.RebootUtil.*;

public class Rebooter {

    public static void main(String[] args) {
        useSystemProxies();
        addGenericSSLCertificate();


        ScheduledExecutorService pool = newScheduledThreadPool(1);

        Runnable action = () -> {
            try {
                Map<HostName, ZonedDateTime> rebootTimes = readRebootTimes();

                System.out.println(ZonedDateTime.now() + ": " + rebootTimes);

                HostName actualHostname = HostName.localHostName();
                for (Map.Entry<HostName, ZonedDateTime> entry : rebootTimes.entrySet()) {
                    HostName hostName = entry.getKey();
                    ZonedDateTime rebootTime = entry.getValue();

                    if (actualHostname.equals(hostName)) {
                        ZonedDateTime now = ZonedDateTime.now();
                        if (rebootTime.isAfter(now)) {
                            triggerRebootAt(rebootTime);
                        }
                    }
                }
            } catch (Exception e) {
                e.printStackTrace();
            }
        };

        pool.scheduleAtFixedRate(action, 0, 5, TimeUnit.MINUTES);
    }
}
