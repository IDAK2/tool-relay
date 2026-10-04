import type{Metadata}from'next';import'./tokens.css';import'./globals.css';
export const metadata:Metadata={title:'Tool Relay',description:'A validator-governed community tool lending workshop on GenLayer.'};
export default function Layout({children}:{children:React.ReactNode}){return <html lang="en"><body>{children}</body></html>}
