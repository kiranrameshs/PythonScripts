import { TestBed } from '@angular/core/testing';

import { RoutegaurdService } from './routegaurd.service';

describe('RoutegaurdService', () => {
  let service: RoutegaurdService;

  beforeEach(() => {
    TestBed.configureTestingModule({});
    service = TestBed.inject(RoutegaurdService);
  });

  it('should be created', () => {
    expect(service).toBeTruthy();
  });
});
