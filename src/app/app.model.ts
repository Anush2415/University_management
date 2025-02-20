/*import { NgModule } from '@angular/core';
import { BrowserModule } from '@angular/platform-browser';
import { AppComponent } from './app.component';

@NgModule({
  declarations: [
    // No declarations for standalone components
  ],
  imports: [
    BrowserModule,
    AppComponent // Import standalone AppComponent here
  ],
  providers: [],
  bootstrap: [AppComponent] // Root component
})
export class AppModule { }
*/
import { NgModule } from '@angular/core';
import { BrowserModule } from '@angular/platform-browser';

@NgModule({
  imports: [
    BrowserModule,
    // Add other modules here if needed
  ],
  providers: [
    // Add services or providers here if needed
  ],
})
export class AppModule { }
