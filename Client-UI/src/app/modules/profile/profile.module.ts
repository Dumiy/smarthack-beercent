import { NgModule } from '@angular/core';
import { SharedModule } from '../shared/shared.module';
import { ProfileComponent } from './components/profile/profile.component';

@NgModule({
    declarations: [ProfileComponent],
    imports: [
        SharedModule
    ],
    exports: [ProfileComponent],
    providers: [],
})
export class ProfileModule {}
