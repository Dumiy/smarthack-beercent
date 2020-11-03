import { NgModule } from '@angular/core';
import { SharedModule } from '../shared/shared.module';
import { ProductModule } from '../product/product.module';
import { HistoryComponent } from './components/history/history.component';

@NgModule({
    declarations: [HistoryComponent],
    imports: [
        SharedModule,
        ProductModule
    ],
    exports: [HistoryComponent],
    providers: [],
})
export class HistoryModule {}
