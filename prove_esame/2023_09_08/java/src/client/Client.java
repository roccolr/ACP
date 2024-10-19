package client;

import java.util.Hashtable;
import javax.jms.*;
import javax.jms.Topic;
import javax.naming.Context;
import javax.naming.InitialContext;
import javax.naming.NamingException;
import java.util.Random;


public class Client {
    public static void main(String[] args) {
        final int numRichieste = 40;
        Hashtable <String, String> prop = new Hashtable<>();
        Random r = new Random();
        

        prop.put("java.naming.factory.initial", "org.apache.activemq.jndi.ActiveMQInitialContextFactory");
        prop.put("java.naming.provider.url", "tcp://127.0.0.1:61616");
        prop.put("topic.data", "dataTopic");

        try{
            Context jndiContext = new InitialContext(prop);

            //otteniamo gli administered objects
            TopicConnectionFactory topicConnectionFactory = (TopicConnectionFactory)jndiContext.lookup("TopicConnectionFactory");
            Topic data = (Topic)jndiContext.lookup("data");
            

            //otteniamo una connessione
            TopicConnection topicConnection = topicConnectionFactory.createTopicConnection();

            //otteniamop una sessione
            TopicSession session = topicConnection.createTopicSession(false, Session.AUTO_ACKNOWLEDGE);

            //otteniamo un publisher
            TopicPublisher publisher = session.createPublisher(data);
            MapMessage msg = session.createMapMessage();
            for(int i=0; i<numRichieste; i++){
                if(i%2 == 0){
                    msg.setString("type", "temperature");
                    msg.setInt("value", (int)(Math.random()*100));
                    publisher.publish(msg);
                }else{
                    msg.setString("type", "pressure");
                    msg.setInt("value", (r.nextInt(50)+1000));
                    publisher.publish(msg);
                }
                Thread.sleep(100);
            }

            System.out.format("[CLIENT]\tpubblicati %d messaggi", numRichieste);

            publisher.close();
            session.close();
            topicConnection.close();

        }catch(NamingException e){
            e.printStackTrace();
        }catch(JMSException e){
            e.printStackTrace();
        }catch(InterruptedException e){
            e.printStackTrace();
        }

    }
}

/*
 * 
 * "java.naming.factory.initial" -> "org.apache.activemq.jndi.ActiveMQInitialContextFactory"``
* ``"java.naming.provider.url" -> "tcp://127.0.0.1:61616"``
 * 
 * 
 */
