import '../styles/globals.css'
import type { AppProps } from 'next/app'
import { ChakraProvider, Container,Box } from "@chakra-ui/react";

function MyApp({ Component, pageProps }: AppProps) {
  return (
    <ChakraProvider>
      <Box bgColor="gray.50">
        <Container maxW="container.lg" bgColor="white"  minH="100vh">
          <Component {...pageProps} />
        </Container>
      </Box>
		</ChakraProvider>
	);
}

export default MyApp
