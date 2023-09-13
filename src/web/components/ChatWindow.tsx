'use client'

import { Card, TextArea } from '@radix-ui/themes';
import { Button} from '@radix-ui/themes';
import useSWR from 'swr'

const fetcher = (url: RequestInfo | URL) => fetch(url).then(r => r.json())

const Chatbot = () => {
  const { data, error, isLoading } = useSWR('/.auth/me', fetcher)
  let hello
  if (isLoading) {
    hello = <div>loading...</div>
  } else {
    hello = <div>Hello {data.clientPrincipal.userDetails}</div>
  }
  return (
    <div className="flex flex-col h-screen space-y-4 p-8">
      <Card className="grow">
        {hello}
      </Card>
      <div className="flex flex-row items-center space-x-4">
        <div className="grow content-center">
          <TextArea></TextArea>
        </div>
        <Button size="4" className="w-32">Send</Button>
      </div>
    </div>
  );
};

export default Chatbot;
