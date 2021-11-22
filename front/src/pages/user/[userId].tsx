import { useRouter } from "next/router"
import React from "react"

export default function UserPage() {
  const {query} = useRouter()
  const { userId } = query
  return (
    <div>
      UserId: {userId}
    </div>
  )
}
