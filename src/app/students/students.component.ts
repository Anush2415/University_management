import { Component } from '@angular/core';

@Component({
  selector: 'app-students',
  standalone: true,
  templateUrl: './students.component.html',
  styleUrls: ['./students.component.css']
})
export class StudentsComponent {

  fetchStudentDetails() {
    const studentId = (document.getElementById('studentIdInput') as HTMLInputElement).value;

    if (studentId.trim() === "") {
      alert("Please enter a valid Student ID");
      return;
    }

    const requestOptions: RequestInit = {
      method: 'GET',
      redirect: 'follow'
    };

    fetch(`http://127.0.0.1:8000/student_list/?student_id=${studentId}`, requestOptions)
      .then(response => response.json())
      .then(data => {
        const tableBody = document.getElementById('studentTableBody');
        if (tableBody) {
          tableBody.innerHTML = '';
          if (data.length > 0) {
            data.forEach((student: any) => {
              const row = document.createElement('tr');
              row.innerHTML = `
                <td>${student.student_id}</td>
                <td>${student.first_name}</td>
                <td>${student.last_name}</td>
                <td>${student.email}</td>
                <td>${student.department_id}</td>
                <td>${student.course_id}</td>
                <td>${student.semester_id}</td>
                <td>${student.enrollment_start_date}</td>
                <td>${student.enrollment_end_date}</td>
              `;
              tableBody.appendChild(row);
            });
            document.getElementById('studentDetailsTable')?.classList.remove('hidden');
          } else {
            alert("No student found with the provided ID.");
          }
        }
      })
      .catch(error => console.error('Error:', error));
  }

  toggleAddStudentForm() {
    const form = document.getElementById('addStudentForm');
    form?.classList.toggle('hidden');
  }

  addStudent() {
    const form = document.getElementById('addStudentForm') as HTMLFormElement;
    const formData = new FormData(form);
    const studentData: any = {
      student_id: formData.get('student_id'),
      first_name: formData.get('first_name'),
      last_name: formData.get('last_name'),
      email: formData.get('email'),
      department_id: formData.get('department_id'),
      course_id: formData.get('course_id')
    };

    for (const [key, value] of Object.entries(studentData)) {
      if (!value) {
        alert(`Please fill out the ${key.replace('_', ' ')} field.`);
        return;
      }
    }

    const requestOptions: RequestInit = {
      method: 'POST',
      headers: { 'Content-Type': 'application/json' },
      body: JSON.stringify(studentData)
    };

    fetch('http://127.0.0.1:8000/add_student/', requestOptions)
      .then(response => response.json())
      .then(result => {
        console.log("Result:", result); // Add debugging here
        alert("Student added successfully!");
        form.reset();
        document.getElementById('addStudentForm')?.classList.add('hidden');
      })
      .catch(error => {
        console.error('Error:', error);
        alert('An error occurred while adding the student.');
      });
  }
}
