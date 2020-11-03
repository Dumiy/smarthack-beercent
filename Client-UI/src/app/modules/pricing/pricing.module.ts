import { NgModule } from '@angular/core';
import { PricingComponent } from './components';
import { SharedModule } from '../shared/shared.module';

@NgModule({
    declarations: [PricingComponent],
    imports: [
        SharedModule
    ],
    exports: [PricingComponent],
    providers: [],
})
export class PricingModule {}
