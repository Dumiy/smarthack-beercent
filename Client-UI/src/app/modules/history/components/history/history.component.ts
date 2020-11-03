import { Component, OnInit } from '@angular/core';

@Component({
  selector: 'app-history',
  templateUrl: './history.component.html',
  styleUrls: ['./history.component.scss']
})
export class HistoryComponent implements OnInit {
  productList = [
    {
      name: 'Laptop GL552',
      url: 'https://compari.ro',
      score: 4.8
    },
    {
      name: 'Samsung A7 2018',
      url: 'https://compari.ro',
      score: 4.1
    },
    {
      name: 'Samsung Galaxy Buds',
      url: 'https://compari.ro',
      score: 3.2
    },
    {
      name: 'Allview Naspa',
      url: 'https://compari.ro',
      score: 1.3
    },
    {
      name: 'Smartphone Asus Zenfone',
      url: 'https://compari.ro',
      score: 4.3
    },
    {
      name: 'Smartwatch Fitbit 2020',
      url: 'https://compari.ro',
      score: 4.9
    },
    {
      name: 'Mouse Razer',
      url: 'https://compari.ro',
      score: 3.2
    },
    {
      name: 'Mouse A+',
      url: 'https://compari.ro',
      score: 1.5
    },
    {
      name: 'Laptop Asus Tuf',
      url: 'https://compari.ro',
      score: 3.9
    },
    {
      name: 'Smartphone Huawei',
      url: 'https://compari.ro',
      score: 2.6
    }
  ];
  constructor() { }

  ngOnInit(): void {
  }

}
