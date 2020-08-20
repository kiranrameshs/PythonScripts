import { Component, OnInit } from '@angular/core';
import {TodoDataService} from '../service/data/todo-data.service'
import { Router } from '@angular/router';

export class Todo{
  constructor(
    public id: number,
    public description: string,
    public done: boolean,
    public targetDate:Date ){
  }
}


@Component({
  selector: 'app-list-todos',
  templateUrl: './list-todos.component.html',
  styleUrls: ['./list-todos.component.css']
})
export class ListTodosComponent implements OnInit {

  todos: Todo[]

  message: string;
  // todos=[
  //   {id: 1,description: 'Learn to dance'},
  //   {id: 2,description: 'Learn Angular'}
  // ]

  // todos=[
  //   new Todo(1,'Learn to dance',false, new Date()),
  //   new Todo(2,'Learn Angular',false, new Date()),
  //   new Todo(3,'Learn JavaScript',false, new Date())
  // ]

  // todo = {
  //   id: 1,
  //   description: 'Learn to dance'
  // }
  constructor(private todoservice: TodoDataService,
    private router: Router) { }

  ngOnInit() {
    this.refreshTodos();
  }

  refreshTodos() {
    this.todoservice.retrieveAllTodos('kiran').subscribe(
      response => {
        console.log(response);
        this.todos = response;
      }
    )
  }

  handleDeleteTodo(id){
    this.todoservice.deleteTodo('kiran',id).subscribe(
      response => {
        console.log(response);
        this.message = `Delete of ${id} Successful`;
        this.refreshTodos();
      }
    )
  }

  handleUpdateTodo(id){
      this.router.navigate(['todos',id])
      }

      handleAddTodo(){
        this.router.navigate(['todos',-1])
      }



}
