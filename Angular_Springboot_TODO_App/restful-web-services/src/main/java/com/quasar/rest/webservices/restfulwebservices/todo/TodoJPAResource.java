package com.quasar.rest.webservices.restfulwebservices.todo;


import org.springframework.beans.factory.annotation.Autowired;
import org.springframework.http.HttpStatus;
import org.springframework.http.ResponseEntity;
import org.springframework.web.bind.annotation.*;
import org.springframework.web.servlet.support.ServletUriComponentsBuilder;

import java.net.URI;
import java.util.List;

@CrossOrigin(origins = "http://localhost:4200")
@RestController
public class TodoJPAResource {
    @Autowired
    private todoHardCodedService todoService;

    @Autowired
    private TodoJPARepository todoJPARepository;

    @GetMapping("/jpa/users/{username}/todos")
    public List<Todo> getAllTodos(@PathVariable String username)
    {
        return todoJPARepository.findByUsername(username);
        //return todoService.findall();
    }

    @DeleteMapping("/jpa/users/{username}/todos/{id}")
    public ResponseEntity<Void> deleteTodo(@PathVariable String username,@PathVariable long id) {
        todoJPARepository.deleteById(id);
        return ResponseEntity.noContent().build();

    }

    @GetMapping("/jpa/users/{username}/todos/{id}")
    public Todo getTodo(@PathVariable String username, @PathVariable long id)
    {
        return todoJPARepository.findById(id).get();
        //return (todoService.findById(id));
    }

    @PutMapping("/jpa/users/{username}/todos/{id}")
    public ResponseEntity<Todo>updateTodo(@PathVariable String username,@PathVariable long id, @RequestBody Todo todo) {
        Todo updatedTodo = todoJPARepository.save(todo);
        return new ResponseEntity<Todo>(todo, HttpStatus.OK);
    }


    @PostMapping("/jpa/users/{username}/todos")
    public ResponseEntity<Todo>createTodo(@PathVariable String username, @RequestBody Todo todo) {
        //Todo createdTodo = todoService.save(todo);
        todo.setUsername(username);
        Todo createdTodo = todoJPARepository.save(todo);
        //get current resource url and append new id
        URI uri=ServletUriComponentsBuilder.fromCurrentRequest().path("/{id}").buildAndExpand(createdTodo.getId()).toUri();


        return ResponseEntity.created(uri).build();
    }


}
