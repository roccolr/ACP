package manager;

import javax.jms.*;

public class RequestListener implements MessageListener{

    private TopicSession session;
    private Topic compraTopic;
    private Topic vendiTopic;
    
    public RequestListener(TopicSession s, Topic c, Topic v){
        session = s;
        compraTopic = c;
        vendiTopic = v;
    }

    public void onMessage(Message msg){
        MapMessage msgReceived = (MapMessage)msg;

        try{
            String tipologia = msgReceived.getString("tipo");
            String value = msgReceived.getString("valore");


            if(tipologia.equalsIgnoreCase("compra")){
                TopicPublisher cPublisher = session.createPublisher(compraTopic);
                TextMessage msgToSend = session.createTextMessage();
                msgToSend.setText(value);
                cPublisher.send(msgToSend);
                System.out.println("[MANAGER]\tinviato sulla coda compra il messaggio: "+msgToSend.getText());    
            }else if(tipologia.equalsIgnoreCase("vendi")){
                TopicPublisher vPublisher = session.createPublisher(vendiTopic);
                TextMessage msgToSend = session.createTextMessage();
                msgToSend.setText(value);
                vPublisher.send(msgToSend);
                System.out.println("[MANAGER]\tinviato sulla coda vendi il messaggio: "+msgToSend.getText());    
            }

        }catch (JMSException e){
            e.printStackTrace();
        }

    }
}
