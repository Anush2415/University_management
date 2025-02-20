import { Component } from '@angular/core';

@Component({
  selector: 'app-header',
  standalone: true,
  templateUrl: './header.component.html',
  styleUrls: ['./header.component.css']
})
export class HeaderComponent {
  showSection(section: string) {
    document.querySelectorAll('main > section').forEach(section => {
      section.classList.add('hidden');
    });
    document.getElementById(section)?.classList.remove('hidden');
  }
}
