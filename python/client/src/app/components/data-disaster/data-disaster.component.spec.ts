import { async, ComponentFixture, TestBed } from '@angular/core/testing';

import { DataDisasterComponent } from './data-disaster.component';

describe('DataDisasterComponent', () => {
  let component: DataDisasterComponent;
  let fixture: ComponentFixture<DataDisasterComponent>;

  beforeEach(async(() => {
    TestBed.configureTestingModule({
      declarations: [ DataDisasterComponent ]
    })
    .compileComponents();
  }));

  beforeEach(() => {
    fixture = TestBed.createComponent(DataDisasterComponent);
    component = fixture.componentInstance;
    fixture.detectChanges();
  });

  it('should create', () => {
    expect(component).toBeTruthy();
  });
});
