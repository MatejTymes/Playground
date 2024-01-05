plugins {
    id("java")
}

group = "co.uk.mtymes"
version = "1.0-SNAPSHOT"

repositories {
    mavenCentral()
}

dependencies {

    implementation("com.github.matejtymes:javafixes:1.3.7.1")
    implementation("com.google.guava:guava:31.1-jre")
    implementation("org.apache.pdfbox:pdfbox:3.0.1")


    testImplementation(platform("org.junit:junit-bom:5.9.1"))
    testImplementation("org.junit.jupiter:junit-jupiter")
    testImplementation("org.hamcrest:hamcrest-all:1.3")
}

tasks.test {
    useJUnitPlatform()
}