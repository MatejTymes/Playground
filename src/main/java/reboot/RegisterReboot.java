package reboot;

import java.time.ZoneId;
import java.time.ZonedDateTime;

public class RegisterReboot {



    public static void main(String[] args) {
        String machineName = "GBD03740185";
        ZonedDateTime rebootIn = ZonedDateTime.now().plusMinutes(10).withZoneSameInstant(ZoneId.of("UTC"));

        System.out.println(machineName + "|" + rebootIn);
    }
}
