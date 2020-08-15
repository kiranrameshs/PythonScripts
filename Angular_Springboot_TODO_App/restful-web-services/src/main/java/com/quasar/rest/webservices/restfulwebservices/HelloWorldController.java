package com.quasar.rest.webservices.restfulwebservices;

import org.springframework.web.bind.annotation.GetMapping;
import org.springframework.web.bind.annotation.RequestMapping;
import org.springframework.web.bind.annotation.RequestMethod;
import org.springframework.web.bind.annotation.RestController;

@RestController
public class HelloWorldController {


    @GetMapping(path = "/hello-world")
    public String helloWorld(){
        return "Hello World";
    }

    //return bean
    @GetMapping(path = "/hello-world-bean")
    public helloWorldBean helloWorldBean(){
        return (new helloWorldBean("Hello World"));
    }

}
