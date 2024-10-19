package pubsub;

import java.util.Hashtable;

import javax.jms.*;
import javax.naming.*;

public class Publisher {
    public static void main(String argv[]){
        Hashtable <String,String> prop = new Hashtable<>();
        prop.put("java.naming.factory.initial", "org.apache.activemq.jndi.ActiveMQInitialContextFactory");
        prop.put("java.naming.provider.url", "tcp://127.0.0.1:61616");
        prop.put("topic.soccer", "soccernews");
        prop.put("topic.tennis", "tennisnews");

        try{

            Context jndiContext = new InitialContext(prop);
            TopicConnectionFactory tcf = (TopicConnectionFactory)jndiContext.lookup("TopicConnectionFactory");
            Topic soccerTopic = (Topic)jndiContext.lookup("soccer");
            Topic tennisTopic = (Topic)jndiContext.lookup("tennis");

            TopicConnection conn = tcf.createTopicConnection();
            TopicSession session = conn.createTopicSession(false, Session.AUTO_ACKNOWLEDGE);

            TopicPublisher pub = session.createPublisher(tennisTopic);

            TextMessage msg = session.createTextMessage("Messaggio di prova");
            msg.setIntProperty("propInt", 69420);

            pub.send(msg);

            System.out.println("\nMessage JMSMessageID " + msg.getJMSMessageID());
            System.out.println("Message JMSCorrelationID " + msg.getJMSCorrelationID()); // not set
            System.out.println("Message JMSDeliveryMode " + msg.getJMSDeliveryMode()); //PERSISTENT, NON-PERSISTENT
            System.out.println("Message JMSExpiration " + msg.getJMSExpiration());
            System.out.println("Message JMSPriority " + msg.getJMSPriority());
            System.out.println("Message JMSReplyTo " + msg.getJMSReplyTo());

            pub.close();
            session.close();
            conn.close();
        }catch(NamingException e){
            e.printStackTrace();
        }catch(JMSException e){
            e.printStackTrace();
        }
    }
}
