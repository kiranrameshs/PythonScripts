import { Component, OnInit } from '@angular/core';
import {TodoDataService} from '../service/data/todo-data.service';
import { Todo } from '../list-todos/list-todos.component';
import { ActivatedRoute, Router } from '@angular/router';
import { BasicAuthenticationService } from '../service/basic-authentication.service';

@Component({
  selector: 'app-todo',
  templateUrl: './todo.component.html',
  styleUrls: ['./todo.component.css']
})
export class TodoComponent implements OnInit {

  id: number;
  todo: Todo;
  username:string;
  
  constructor(private todoservice: TodoDataService,
    private route:ActivatedRoute,
    private router: Router,
    private basicAuthenticationService: BasicAuthenticationService ) { }

  ngOnInit() {
    this.id = this.route.snapshot.params['id']
    this.todo = new Todo (this.id,'',false,new Date());
    this.username = this.basicAuthenticationService.getAuthenticatedUser();

    if(this.id!=-1){
      this.todoservice.retrieveTodo(this.username,this.id).subscribe(
        data => this.todo = data
      )
    }
  }

  saveTodo(){
    if(this.id== -1){
      //create
      this.todoservice.addTodo(this.username, this.todo).subscribe(
        data => {console.log(data)
        this.router.navigate(['todos'])
        }
      )

    }
    else{
      //update
    this.todoservice.updateTodo(this.username,this.id, this.todo).subscribe(
      data => {console.log(data)
      this.router.navigate(['todos'])
      }
    )
    }
  }

}
