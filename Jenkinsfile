node{
    def app
        stage('Cloning Repository') {
            checkout scm
        }
        stage('Testing Code')
        {
                sh 'python3 test.py'  
        }
        stage('Containerizing')
        {
                app = docker.build("ankitpd/project_approval_system")
        }
        stage('Pushing Image')
      {
        docker.withRegistry('https://registry.hub.docker.com', 'docker-hub-credentials') {
            app.push("${env.BUILD_NUMBER}")
            app.push("latest")
        }
      }
    stage('Deploying')
    {
        build job: 'deploy_pas'
    }
}
