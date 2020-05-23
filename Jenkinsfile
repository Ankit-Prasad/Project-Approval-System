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
    stage('Deploying on Localhost')
      {
        step([
            $class: "RundeckNotifier",
            rundeckInstance: "rundeck",
            jobId: "78640273-d666-4b8b-a94f-0b613f36955e",
            includeRundeckLogs: true,
            shouldWaitForRundeckJob: true,
            shouldFailTheBuild: true,
            tailLog: true
        ])
      }
}
