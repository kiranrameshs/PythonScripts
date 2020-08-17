package com.quasar.rest.webservices.restfulwebservices.basic.auth;

public class AuthenticationBean {
    private String message;

    public AuthenticationBean() {
    }

    public AuthenticationBean(String message) {
        this.message = message;
    }

    public void setMessage(String message) {
        this.message = message;
    }

    @Override
    public String toString() {
        return "helloWorldBean{" +
                "message='" + message + '\'' +
                '}';
    }

    public String getMessage() {
        return message;
    }
}
