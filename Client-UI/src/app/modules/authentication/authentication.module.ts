import { NgModule } from '@angular/core';
import { LoginComponent } from './components';
import { SharedModule } from '../shared/shared.module';
import { RegisterComponent } from './components/register/register.component';
import { LandingPageComponent } from './components/landing-page/landing-page.component';

@NgModule({
    declarations: [
        LoginComponent,
        RegisterComponent,
        LandingPageComponent
    ],
    imports: [
        SharedModule
    ],
    exports: [
        LoginComponent,
        RegisterComponent
    ],
    providers: [],
})
export class AuthenticationModule {}
