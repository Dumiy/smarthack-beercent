import { NgModule } from '@angular/core';
import { Routes, RouterModule } from '@angular/router';
import { LoginComponent } from './modules/authentication/components';
import { FindComponent } from './modules/find/components';
import { AuthGuard, LandingGuard } from './modules/shared/services';
import { PricingComponent } from './modules/pricing/components';
import { LandingPageComponent } from './modules/authentication/components/landing-page/landing-page.component';
import { ProfileComponent } from './modules/profile/components/profile/profile.component';
import { HistoryModule } from './modules/history/history.module';
import { HistoryComponent } from './modules/history/components/history/history.component';

const routes: Routes = [
  {
    path: '',
    component: LandingPageComponent,
    canActivate: [LandingGuard]
  },
  {
    path: 'landing-page',
    component: LandingPageComponent,
    canActivate: [LandingGuard]
  },
  {
    path: 'find',
    component: FindComponent,
    canActivate: [AuthGuard]
  },
  {
    path: 'analytics',
    component: FindComponent,
    canActivate: [AuthGuard]
  },
  {
    path: 'profile',
    component: ProfileComponent,
    canActivate: [AuthGuard]
  },
  {
    path: 'history',
    component: HistoryComponent,
    canActivate: [AuthGuard]
  },
  {
    path: 'pricing',
    component: PricingComponent,
    canActivate: [AuthGuard]
  },
  {
    path: 'about',
    component: PricingComponent,
    canActivate: [AuthGuard]
  },
  {
    path: 'terms',
    component: PricingComponent,
    canActivate: [AuthGuard]
  },
  { path: '**', redirectTo: '' }
];

@NgModule({
  imports: [RouterModule.forRoot(routes)],
  exports: [RouterModule]
})
export class AppRoutingModule { }
