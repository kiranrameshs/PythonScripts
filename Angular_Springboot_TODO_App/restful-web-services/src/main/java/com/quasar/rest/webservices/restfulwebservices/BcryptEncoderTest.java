package com.quasar.rest.webservices.restfulwebservices;

import org.springframework.security.crypto.bcrypt.BCryptPasswordEncoder;

public class BcryptEncoderTest {
    public static void main(String[] args){
        BCryptPasswordEncoder encoder = new BCryptPasswordEncoder();
//        String encodedString = encoder.encode("password@123");
        for (int i = 1; i < 10; i++) {
            String encodedString = encoder.encode("password@123");
            System.out.println("encodedString is "+encodedString);
        }
    }
}
