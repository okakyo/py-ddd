import { Container } from "@chakra-ui/layout";
import React from "react";

type TheLayoutProps = {
  children: React.ReactNode
}

export const TheLayout = ({children}:TheLayoutProps) => {
  return (
    <>
      <Container>
        {children}
      </Container>
    </>
  )
}
