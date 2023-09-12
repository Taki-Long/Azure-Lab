import { Box, Grid, Flex, Container, Card } from '@radix-ui/themes'
import Chatbot from '@/components/ChatWindow'

export default function Home() {
  return (
    <Flex gap="3">
      <Flex width="9" className="bg-slate-200" direction="column" gap="3">
        <Card>
        </Card>
      </Flex>
      <Flex width="100%" direction="column" gap="3">
        <Card>
          <Chatbot />
        </Card>
      </Flex>
    </Flex>

  )
}