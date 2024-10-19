package dispatcher;

import javax.jms.*;

public class DispatcherThread extends Thread{
    //Deve capire il messaggio, chiamare la funzione giusta, e inserire sulla coda di ritorno il messaggio
    TextMessage msg;
    QueueConnection conn;

    public DispatcherThread(TextMessage msg, QueueConnection conn){
        this.msg = msg; //dal messaggio risaliamo alla coda
        this.conn = conn;
    }

    public void run(){
        //interpreto il messaggio
        try{
            String text = msg.getText();
            DispatcherProxy proxy = new DispatcherProxy();
            Queue RispQueue = (Queue)msg.getJMSReplyTo();

            //creiamo la sessione
            QueueSession session = conn.createQueueSession(false, Session.AUTO_ACKNOWLEDGE);
            QueueSender sender = session.createSender(RispQueue);
            
            String [] spliitedText = text.split("-");
            String msg = "something went wrong";
            if(spliitedText[0].equals("deposita")){
                int val = Integer.parseInt(spliitedText[1]);
                proxy.deposita(val);
                msg = "Deposited";
            }
            else if(spliitedText[0].equals("preleva")){
                int val = proxy.preleva();
                msg = Integer.toString(val);
            }

            TextMessage ResponseMessage = session.createTextMessage(msg);
            sender.send(ResponseMessage);

            sender.close();
            session.close();
            
        }catch(JMSException e){
            e.printStackTrace();
        }
        
    }
}
