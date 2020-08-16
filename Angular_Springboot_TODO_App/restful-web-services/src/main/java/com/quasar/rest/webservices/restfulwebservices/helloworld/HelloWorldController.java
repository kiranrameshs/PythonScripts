package com.quasar.rest.webservices.restfulwebservices;

import org.springframework.web.bind.annotation.*;
@CrossOrigin(origins = "http://localhost:4200")
@RestController
public class HelloWorldController {


    @GetMapping(path = "/hello-world")
    public String helloWorld(){
        return "Hello World";
    }

    //return bean
    @GetMapping(path = "/hello-world-bean")
    public helloWorldBean helloWorldBean(){
        //throw new RuntimeException("Some error occured, contact support");
        return (new helloWorldBean("Hello World - changed"));
    }

    //return bean
    @GetMapping(path = "/hello-world/path-variable/{name}")
    public helloWorldBean helloWorldPathVariable(@PathVariable String name)
    {
        return (new helloWorldBean(String.format("Hello World, %s ", name)));
    }
}
