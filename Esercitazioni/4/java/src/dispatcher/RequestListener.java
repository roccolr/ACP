package dispatcher;
import javax.jms.*;


public class RequestListener implements MessageListener {
    private QueueSession session;
    private ServerProxy proxy;
    
    public RequestListener(QueueSession session, ServerProxy proxy){
        this.session = session;
        this.proxy = proxy;
    }

    @Override
    public void onMessage(Message message) {
        try{
            TextMessage msg = (TextMessage)message;
            Queue risposta = (Queue)message.getJMSReplyTo();
            String txtFromClient = msg.getText();
            System.out.println("[DISPATCHER]\tricevuta richiesta "+txtFromClient);
            String [] splittedMessage = txtFromClient.split("-");
            if(splittedMessage[0].equals("deposita")){
                DispatcherThread t = new DispatcherThread(false, risposta, session, proxy, Integer.parseInt(splittedMessage[1]));
                t.start();
            }else if(splittedMessage[0].equals("preleva")){
                DispatcherThread t = new DispatcherThread(true, risposta, session, proxy, -1);
                t.start();
            }

        }catch(JMSException e){
            e.printStackTrace();
        }


        
    }
}
