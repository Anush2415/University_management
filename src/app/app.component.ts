import { Component } from '@angular/core';
import { HeaderComponent } from './header/header.component';
import { AboutComponent } from './about/about.component';
import { CoursesComponent } from './courses/courses.component';
import { StudentsComponent } from './students/students.component';

@Component({
  selector: 'app-root',
  standalone: true,
  templateUrl: './app.component.html',
  styleUrls: ['./app.component.css'],
  imports: [
    HeaderComponent,
    AboutComponent,
    CoursesComponent,
    StudentsComponent
  ]
})
export class AppComponent {
  title = 'university_website';
}
