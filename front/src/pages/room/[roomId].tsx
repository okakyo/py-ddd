import { Box } from "@chakra-ui/layout";
import { useRouter } from "next/router";
import React from "react";

export default function ChatRoomPage() {
  const {query} = useRouter()
  const { roomId } = query
  return (
      <Box>
        sample
      </Box>
  )
}
