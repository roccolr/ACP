package client;

import javax.jms.*;

public class ExtractorListener implements MessageListener{
    Topic press;
    Topic temp;
    TopicConnection conn;
    TopicSession session;

    public ExtractorListener(Topic temp, Topic press, TopicConnection conn, TopicSession session){
        this.temp = temp;
        this.press = press;
        this.conn = conn;
        this.session = session;
    }

    public void onMessage(Message m){
        //riceviamo il messaggio e lo decomponiamo
        MapMessage mapMessage = (MapMessage) m;


        try{
            String type = mapMessage.getString("type");
            int value = mapMessage.getInt("value");

            if(type.equals("temperature")){
                TopicPublisher tempPublisher = this.session.createPublisher(this.temp);
                TextMessage msg = session.createTextMessage();
                msg.setText(Integer.toString(value));
                tempPublisher.publish(msg);
                System.out.println("[EXTRACTOR LISTENER]\t pubblicato su temp il valore: " + value);
                tempPublisher.close();
            }else if(type.equals("pressure")){
                TopicPublisher pressPublisher = this.session.createPublisher(this.press);
                TextMessage msg = session.createTextMessage();
                msg.setText(Integer.toString(value));
                pressPublisher.publish(msg);
                System.out.println("[EXTRACTOR LISTENER]\t pubblicato su press il valore: " + value);
                pressPublisher.close();
            }else{
                System.out.println("[EXTRACTOR LISTENER]\terrore, type non riconosciuto");
            }
        }catch(JMSException e){
            e.printStackTrace();
        }
    }


}
