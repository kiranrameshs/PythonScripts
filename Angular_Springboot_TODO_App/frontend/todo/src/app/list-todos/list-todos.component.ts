import { Component, OnInit } from '@angular/core';

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

  // todos=[
  //   {id: 1,description: 'Learn to dance'},
  //   {id: 2,description: 'Learn Angular'}
  // ]

  todos=[
    new Todo(1,'Learn to dance',false, new Date()),
    new Todo(2,'Learn Angular',false, new Date()),
    new Todo(3,'Learn JavaScript',false, new Date())
  ]

  // todo = {
  //   id: 1,
  //   description: 'Learn to dance'
  // }
  constructor() { }

  ngOnInit() {
  }

}
