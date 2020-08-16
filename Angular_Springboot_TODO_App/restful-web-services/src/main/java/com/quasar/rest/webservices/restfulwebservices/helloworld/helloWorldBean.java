package com.quasar.rest.webservices.restfulwebservices.helloworld;

public class helloWorldBean {
    private String message;

    public helloWorldBean() {
    }

    public helloWorldBean(String message) {
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
