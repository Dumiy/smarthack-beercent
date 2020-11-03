import { Component, OnInit, EventEmitter, Output } from '@angular/core';
import { FormControl, FormBuilder, Validators, FormGroup } from '@angular/forms';
import { PRODUCT_TYPES_ARRAY } from '../../models';

@Component({
  selector: 'app-search',
  templateUrl: './search.component.html',
  styleUrls: ['./search.component.scss']
})
export class SearchComponent implements OnInit {
  formGroup: FormGroup;
  searchControl: FormControl = new FormControl();
  keywordsControl: FormControl = new FormControl();
  selectedProductType: any;
  selectedBrand: string = '';
  selectedPrice: string = '';
  @Output()
  searchEmitter: EventEmitter<any> = new EventEmitter<any>();
  constructor(private formBuilder: FormBuilder) { }

  ngOnInit(): void {
    this.initForm();
    this.initSearchSubscribe();
  }

  initForm(): void {
    this.formGroup = this.formBuilder.group({
      ['search']: ['', Validators.required],
      ['keywords']: ['', Validators.pattern('[a-zA-Z0-9]+$|[a-zA-Z0-9]+\,[a-zA-Z0-9]+$')]
    });
  }

  initSearchSubscribe(): void {
    this.formGroup.get('search').valueChanges.subscribe(
      (value: string) => {
        const product = PRODUCT_TYPES_ARRAY.find((product: any) => product.type === value);
        if(product) {
          this.selectedProductType = product;
        }
        else {
          this.selectedProductType = null
          this.selectedBrand = '';
          this.selectedPrice = '';
        }
      }
    )
  }

  emitSearchEvent(): void {
    this.searchEmitter.emit({
      first_key: this.formGroup.get('search').value.toLowerCase(),
      type: this.selectedBrand.toLowerCase(),
      key_word: (this.formGroup.get('keywords').value as string).split(',').join(' ')
    });
  }

}
