import { BrowserModule } from '@angular/platform-browser';
import { NgModule } from '@angular/core';
import { AgmCoreModule } from '@agm/core';
import { AppRoutingModule } from './app-routing.module';
import { AppComponent } from './app.component';
import { MenuComponent } from './components/menu/menu.component';
import { MapComponent } from './components/map/map.component';
import { HttpClientModule} from '@angular/common/http';
import { ReactiveFormsModule, FormsModule } from '@angular/forms';
import { HomeComponent } from './components/home/home.component';
import { ShowdataComponent } from './components/showdata/showdata.component';
import { DataDisasterComponent } from './components/data-disaster/data-disaster.component';

@NgModule({
  declarations: [ 
    AppComponent,
    MenuComponent, 
    MapComponent, 
    HomeComponent, 
    ShowdataComponent, DataDisasterComponent
  ],
  imports: [
    BrowserModule,
    AppRoutingModule,
    ReactiveFormsModule,
    FormsModule,
    HttpClientModule,
    AgmCoreModule.forRoot({
      apiKey: 'AIzaSyCNfEHbve6VbakJjGcUhsag0PQdbp37iNs'
    })
  ],
  providers: [],
  bootstrap: [ AppComponent ]
})
export class AppModule {}