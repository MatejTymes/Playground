package reboot;

import reboot.RebootUtil.HostName;

import java.time.ZoneId;
import java.time.ZonedDateTime;
import java.util.Map;

import static reboot.RebootUtil.readRebootTimes;
import static reboot.RebootUtil.writeRebootTimes;

public class RegisterReboot {

    public static void main(String[] args) throws Exception {
//        HostName machineName = HostName.localHostName();
        HostName machineName = new HostName("GBD03740185");


        Map<HostName, ZonedDateTime> rebootTimes = readRebootTimes();

        ZonedDateTime rebootIn = ZonedDateTime.now().plusMinutes(17).withZoneSameInstant(ZoneId.of("UTC"));
        rebootTimes.put(machineName, rebootIn);

        writeRebootTimes(rebootTimes);

        System.out.println(machineName + "|" + rebootIn);
    }
}
