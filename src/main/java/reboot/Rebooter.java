package reboot;

import java.net.InetAddress;
import java.time.ZonedDateTime;
import java.util.Map;
import java.util.concurrent.ScheduledExecutorService;
import java.util.concurrent.TimeUnit;

import static java.util.concurrent.Executors.newScheduledThreadPool;
import static reboot.RebootUtil.readRebootTimes;
import static reboot.RebootUtil.triggerRebootAt;

public class Rebooter {

    public static void main(String[] args) throws Exception {
        ScheduledExecutorService pool = newScheduledThreadPool(1);

        pool.scheduleAtFixedRate(
                () -> {
                    try {
                        Map<String, ZonedDateTime> rebootTimes = readRebootTimes();

                        System.out.println(ZonedDateTime.now() + ": " + rebootTimes);

                        String actualHostname = InetAddress.getLocalHost().getHostName().split("\\.")[0].toLowerCase();
                        for (Map.Entry<String, ZonedDateTime> entry : rebootTimes.entrySet()) {
                            String hostName = entry.getKey();
                            ZonedDateTime rebootTime = entry.getValue();

                            if (actualHostname.equalsIgnoreCase(hostName)) {
                                ZonedDateTime now = ZonedDateTime.now();
                                if (rebootTime.isAfter(now)) {
                                    triggerRebootAt(rebootTime);
                                }
                            }
                        }
                    } catch (Exception e) {
                        e.printStackTrace();
                    }
                },
                0,
                5,
                TimeUnit.MINUTES
        );
    }
}
