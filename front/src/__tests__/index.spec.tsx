import React from "react";
import { render, fireEvent, waitFor, screen } from "@testing-library/react";
import HomePage from "../pages/index"

import "@testing-library/jest-dom";

describe('HomePage', () => {
  it('Matches the Document', () => {
    const { } = render(
      <HomePage/>
    )
  })
   expect(screen.getByText("Search:")).toBeInTheDocument();
})
