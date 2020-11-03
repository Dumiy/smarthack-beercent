import { BrowserModule } from '@angular/platform-browser';
import { NgModule } from '@angular/core';

import { AppRoutingModule } from './app-routing.module';
import { AppComponent } from './app.component';
import { BrowserAnimationsModule } from '@angular/platform-browser/animations';
import { SharedModule } from './modules/shared/shared.module';
import { ApiModule } from './api/api.module';
import { FindModule } from './modules/find/find.module';
import { AuthenticationModule } from './modules/authentication/authentication.module';
import { PricingModule } from './modules/pricing/pricing.module';
import { ProductModule } from './modules/product/product.module';
import { ProfileModule } from './modules/profile/profile.module';
import { HistoryModule } from './modules/history/history.module';
@NgModule({
  declarations: [
    AppComponent
  ],
  imports: [
    ApiModule,
    BrowserModule,
    AppRoutingModule,
    BrowserAnimationsModule,
    FindModule,
    AuthenticationModule,
    PricingModule,
    ProductModule,
    ProfileModule,
    HistoryModule,
    SharedModule
  ],
  providers: [],
  bootstrap: [AppComponent]
})
export class AppModule { }
