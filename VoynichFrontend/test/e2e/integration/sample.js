/* eslint-disable */

describe("Sample tests", () => {
  it("Visits index page", () => {
    cy.visit("/");
    cy.contains("div", "Vuetify");
  });

  //  it('Go to about page', () => {
  //    cy.get('a.about-link').click();
  //    cy.contains('h1', 'About');
  //  });
});
