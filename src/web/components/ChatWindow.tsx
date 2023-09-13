'use client'
import { useState } from 'react';
import { Card, TextArea } from '@radix-ui/themes';
import { Button} from '@radix-ui/themes';
import useSWR from 'swr'
import { json } from 'stream/consumers';

const fetcher = (url: RequestInfo | URL) => fetch(url).then(r => r.json())


const Chatbot = () => {
  const { data, error, isLoading } = useSWR('/.auth/me', fetcher)
  let userinfo
  if (isLoading) {
    userinfo = <div>loading...</div>
  } else {
    userinfo = <div>User: {data.clientPrincipal.userDetails}</div>
  }

  const [hello, setHello] = useState("");
  const [input, setInput] = useState("hello");

  const handleClick = (event: { preventDefault: () => void; }) => {
    event.preventDefault();

    fetch("/api/hello",{
      method: "POST",
      body: JSON.stringify({
        "name": input
      })
    }).then((r)=>r.text()).then((d)=>setHello(d))
  };
  
  return (
    <div className="flex flex-col h-screen space-y-4 p-8">
      <Card className="grow">
        {userinfo}
        CallApi: {hello}
      </Card>
      <div className="flex flex-row items-center space-x-4">
        <div className="grow content-center">
          <TextArea value={input} onChange={e=>setInput(e.target.value)}></TextArea>
        </div>
        <Button onClick={handleClick} size="4" className="w-32">Send</Button>
      </div>
    </div>
  );
};

export default Chatbot;
