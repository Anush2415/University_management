import { Component } from '@angular/core';

@Component({
  selector: 'app-courses',
  standalone: true,
  templateUrl: './courses.component.html',
  styleUrls: ['./courses.component.css']
})
export class CoursesComponent {

  fetchCourse(event: Event) {
    const selectElement = event.target as HTMLSelectElement;
    const type = selectElement.value;

    const requestOptions: RequestInit = {
      method: 'GET',
      redirect: 'follow'
    };

    fetch(`http://127.0.0.1:8000/course_list/?type=${type}`, requestOptions)
      .then(response => response.json())
      .then(data => {
        const tableBody = type === 'UG' 
          ? document.getElementById('ug_course_table_body') 
          : document.getElementById('pg_course_table_body');

        if (tableBody) {
          tableBody.innerHTML = '';
          data.forEach((course: any) => {
            const row = document.createElement('tr');
            row.innerHTML = `
              <td>${course.course_id}</td>
              <td>${course.department_id}</td>
              <td>${course.name}</td>
            `;
            tableBody.appendChild(row);
          });
          this.showCourse(type === 'UG' ? 'undergraduate' : 'postgraduate');
        } else {
          console.error('Table body not found');
        }
      })
      .catch(error => console.error('Error:', error));
  }

  showCourse(courseId: string) {
    document.querySelectorAll('.sub-section').forEach(subSection => {
      subSection.classList.add('hidden');
    });
    document.getElementById(courseId)?.classList.remove('hidden');
  }
}
