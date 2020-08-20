package com.quasar.rest.webservices.restfulwebservices.todo;

import org.springframework.data.jpa.repository.JpaRepository;
import org.springframework.stereotype.Repository;

import java.util.List;

@Repository
public interface TodoJPARepository extends JpaRepository<Todo, Long> {
    List<Todo> findByUsername(String username);
}
