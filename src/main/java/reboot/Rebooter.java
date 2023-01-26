package reboot;

import java.time.ZoneId;
import java.time.ZonedDateTime;

public class Rebooter {

    public static void main(String[] args) {
        ZonedDateTime initialTime = ZonedDateTime.now().plusMinutes(10).withZoneSameInstant(ZoneId.of("UTC"));

        String rebootIn = initialTime.toString();
        ZonedDateTime parsedTime = ZonedDateTime.parse(rebootIn);

        System.out.println("initialTime = " + initialTime);
        System.out.println("parsedTime  = " + parsedTime);
    }
}
