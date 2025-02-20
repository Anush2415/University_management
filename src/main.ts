import { bootstrapApplication } from '@angular/platform-browser';
import { AppComponent } from './app/app.component';
import { importProvidersFrom } from '@angular/core';
import { BrowserModule } from '@angular/platform-browser';

// Bootstrapping the standalone AppComponent
bootstrapApplication(AppComponent, {
  providers: [
    importProvidersFrom(BrowserModule),
    // Add other providers or modules here if needed
  ],
})
  .catch(err => console.error(err));
