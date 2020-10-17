import { BrowserModule } from '@angular/platform-browser';
import { NgModule } from '@angular/core';
import { AgmCoreModule } from '@agm/core';
import { AppRoutingModule } from './app-routing.module';
import { AppComponent } from './app.component';
import { MapComponent } from './components/map/map.component';
import { HttpClientModule} from '@angular/common/http';
import { ReactiveFormsModule, FormsModule } from '@angular/forms';
import { HomeComponent } from './components/home/home.component';
import { ShowdataComponent } from './components/showdata/showdata.component';


@NgModule({
  declarations: [ 
    AppComponent,
    MapComponent, 
    HomeComponent, 
    ShowdataComponent, 
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